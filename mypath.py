class Path(object):
    @staticmethod
    def db_dir(database):
        if database == 'ucf101':
            # folder that contains class labels
            root_dir = '/data/raw/video'

            # Save preprocess data into output_dir
            output_dir = '/data/preprocess/video'

            return root_dir, output_dir
        elif database == 'video_cls':
            # folder that contains class labels
            root_dir = '/home/nd/workspace/zjc/pytorch/pytorch-video-recognition/data/video_cls'

            # Save preprocess data into output_dir
            output_dir = '/home/nd/workspace/zjc/pytorch/pytorch-video-recognition/data/preprocess/video_cls/'
            return root_dir, output_dir
        elif database == 'hmdb51':
            # folder that contains class labels
            root_dir = '/Path/to/hmdb-51'

            output_dir = '/path/to/VAR/hmdb51'

            return root_dir, output_dir
        else:
            print('Database {} not available.'.format(database))
            raise NotImplementedError

    @staticmethod
    def model_dir():
        return '/home/nd/workspace/zjc/pytorch/pytorch-video-recognition/model/c3d-pretrained.pth'
