import packagetracker
tracker = packagetracker.PackageTracker()
package = tracker.package('1Z90A26F9003214682')
info = package.track()
print(info.weight)
print(info.service)

