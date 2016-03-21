Title: NSPort delegate
Date: 2014-05-12 12:00
Slug: nsport-delegate


It all started with an intermittent crash.  `NSZombieEnabled` has helped to obtain “message sent to deallocated object” crash report with nice stack trace.  And there was `-[PortController handlePortMessage:]` method in stack trace.  I’ve decided it would be an easy fix — just stop being `NSPort` delegate in `-[PortController dealloc]`.  But the fix wasn’t as straightforward as I’ve expected — there was already `port.delegate = nil` in `-[PortController dealloc]`.  So why message was still sent to deallocated delegate?

After some debugging I’ve discovered that `PortController` was deallocated not before `-handlePortMessage:`, but during `-handlePortMessage:`.  When `PortController`’s owner released controller, `PortController` was kept alive only by a secondary thread. `PortController` sent message through `NSPort` on the secondary thread, `-[PortController handlePortMessage:]` was executed on the main thread and during its execution the secondary thread has finished, released and deallocated `PortController`.  And after that deallocated `PortController` was accessed on main thread somewhere in `-handlePortMessage:`.

I’ve fixed the crash by introducing `-[PortController invalidate]`, in which `PortController` stops being a delegate.  And `PortController`’s owner calls `-invalidate` before it releases `PortController`.  Fortunately, it is performed on the main thread, so `-handlePortMessage:` cannot be called during `-[PortController invalidate]`.  And after `-invalidate` `PortController` isn’t a delegate anymore and doesn’t receive `-handlePortMessage:`.
