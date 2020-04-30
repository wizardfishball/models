from __future__ import absolute_import
from __future__ import division
from __future__ import print_function



from inception.dataset import Dataset



class SketchData(Dataset):
  """Sketch data set."""

  def __init__(self, subset):
    super(SketchData, self).__init__('Sketch', subset)

  def num_classes(self):
    """Returns the number of classes in the data set."""
    return 8

  def num_examples_per_epoch(self):
    """Returns the number of examples in the data subset."""
    if self.subset == 'train':
      return 70000*8
    if self.subset == 'validation':
      return 2500*8

  def download_message(self):
    """"""
    print('You have a problem, but Im not sure what happens.')
    
