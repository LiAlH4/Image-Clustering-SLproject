"""
Authors: Wouter Van Gansbeke, Simon Vandenhende
Licensed under the CC BY-NC 4.0 license (https://creativecommons.org/licenses/by-nc/4.0/)
"""
import os


class MyPath(object):
    @staticmethod
    def db_root_dir(database=''):
        db_names = {'cifar-10', 'stl-10', 'cifar-20', 'imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200','mnist','fashion-mnist'}
        assert(database in db_names)

        if database == 'cifar-10':
            return 'dataset/cifar-10/'
        
        elif database == 'cifar-20':
            return '/path/to/cifar-20/'

        elif database == 'stl-10':
            return '/path/to/stl-10/'
        
        elif database in ['imagenet', 'imagenet_50', 'imagenet_100', 'imagenet_200']:
            return '/path/to/imagenet/'

        elif database=='mnist':
            return 'dataset/mnist/'

        elif database=='fashion-mnist':
            return 'dataset/fashion-mnist/'
        
        else:
            raise NotImplementedError
