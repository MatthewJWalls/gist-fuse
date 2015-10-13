#!/usr/bin/env python3

from fuse import FUSE, FuseOSError, Operations

class GistFuse:

    def chmod(self, path, mode):
        """ change attributes """
        return 0

    def chown(self, path, uid, gid):
        """ change owner or group """
        pass
        
    def create(self, path, mode):
        """ create file, return fd """
        self.fd += 1
        return self.fd
        
    def getattr(self, path, fh=None):
        """ return attributes? """
        pass
        
    def getxattr(self, path, name, position=0):
        """ return something """
        pass
        
    def listxattr(self, path):
        """ return all executable files? """
        pass
        
    def mkdir(self, path, mode):
        """ create a directory, no return """
        pass
        
    def open(self, path, flags):
        """ open files, returns an FD number """
        self.fd += 1
        return self.fd

    def read(self, path, size, offset, fh):
        """ read a file, return data """
        pass

    def readdir(self, path, fh):
        """ return directory listing """
        pass

    def readlink(self, path):
        """ return data in a path """
        pass
    
    def removexattr(self, path, name):
        """ remove x perm, no return """
        pass

    def rename(self, old, new):
        """ rename file, no return """
        pass

    def rmdir(self, path):
        """ remove a directory, no return """
        pass
        
    def setxattr(self, path, name, value, options, position=0):
        """ set executable, no return """
        pass
        
    def statfs(self, path):
        """ return stat info for drive """
        return dict(f_bsize=512, f_blocks=4096, f_bavail=2048)

    def symlink(self, target, source):
        """ create symlink, no return """
        pass
    
    def truncate(self, path, length, fh=None):
        """ resizes the file, no return """
        pass

    def unlink(self, path):
        """ unlink file, no return """
        pass

    def utimens(self, path, times=None):
        """ time info, no return """
        pass
        
    def write(self, path, data, offset, fh):
        """ returns length of data written """
        pass
