from torch import nn


##### GENERATOR #####
class Generator(nn.Module):
    '''
    Generator Class
    Values:
        input_dim: the dimension of the input vector, a scalar
        im_chan: the number of channels of the output eeg, a scalar
        hidden_dim: the inner dimension, a scalar
    '''
    def __init__(self, input_dim=68, im_chan=1, hidden_dim=64):
        super(Generator, self).__init__()
        self.input_dim = input_dim
        # Build the neural network
        self.gen = nn.Sequential(
            #### For 3 channels
#             self.make_gen_block(input_dim, hidden_dim * 4,      kernel_size = (1,60), stride = (1,1)),
#             self.make_gen_block(hidden_dim * 4, hidden_dim * 2, kernel_size = (1,60), stride = (1,1)),
#             self.make_gen_block(hidden_dim * 2, hidden_dim,     kernel_size = (1,60), stride = (1,1)),
#             self.make_gen_block(hidden_dim, im_chan,            kernel_size = (3,50), stride = (1,2), padding = (0,2), final_layer=True),
            #### For 22 channels
            self.make_gen_block(input_dim, hidden_dim * 4,      kernel_size = (3,60), stride = (1,1)),
            self.make_gen_block(hidden_dim * 4, hidden_dim * 2, kernel_size = (4,60), stride = (3,1)),
            self.make_gen_block(hidden_dim * 2, hidden_dim,     kernel_size = (3,60), stride = (2,1)),
            self.make_gen_block(hidden_dim, im_chan,            kernel_size = (2,50), stride = (1,2), padding = (0,2), final_layer=True),
        )

    def make_gen_block(self, input_channels, output_channels, kernel_size, stride, padding = 0, final_layer=False):
        '''
        Function to return a sequence of operations corresponding to a generator block of DCGAN;
        a transposed convolution, a batchnorm (except in the final layer), and an activation.
        Parameters:
            input_channels: how many channels the input feature representation has
            output_channels: how many channels the output feature representation should have
            kernel_size: the size of each convolutional filter, equivalent to (kernel_size, kernel_size)
            stride: the stride of the convolution
            final_layer: a boolean, true if it is the final layer and false otherwise 
                      (affects activation and batchnorm)
        '''
        if not final_layer:
            return nn.Sequential(
                nn.ConvTranspose2d(input_channels, output_channels, kernel_size, stride, padding),
                nn.BatchNorm2d(output_channels),
                nn.ReLU(inplace=True),
            )
        else:
            return nn.Sequential(
                nn.ConvTranspose2d(input_channels, output_channels, kernel_size, stride, padding),
                nn.Tanh(),
            )

    def forward(self, noise):
        '''
        Function for completing a forward pass of the generator: Given a noise tensor, 
        returns generated images.
        Parameters:
            noise: a noise tensor with dimensions (n_samples, input_dim)
        '''
        x = noise.view(len(noise), self.input_dim, 1, 1)
        return self.gen(x)


##### Discriminator #####
class Discriminator(nn.Module):
    '''
    Discriminator Class
    Values:
      im_chan: the number of channels of the output eeg, a scalar
      hidden_dim: the inner dimension, a scalar
    '''
    def __init__(self, im_chan=5, hidden_dim=64):
        super(Discriminator, self).__init__()
        self.disc = nn.Sequential(
            self.make_disc_block(im_chan, hidden_dim,        kernel_size = (1,50), stride = (2,4)),
            self.make_disc_block(hidden_dim, hidden_dim * 2, kernel_size = (1,50), stride = (2,4)),
            self.make_disc_block(hidden_dim * 2, 1,          kernel_size = (1,10), stride = (2,1), final_layer=True),
        )

    def make_disc_block(self, input_channels, output_channels, kernel_size, stride, final_layer=False):
        '''
        Function to return a sequence of operations corresponding to a discriminator block of the DCGAN; 
        a convolution, a batchnorm (except in the final layer), and an activation (except in the final layer).
        Parameters:
            input_channels: how many channels the input feature representation has
            output_channels: how many channels the output feature representation should have
            kernel_size: the size of each convolutional filter, equivalent to (kernel_size, kernel_size)
            stride: the stride of the convolution
            final_layer: a boolean, true if it is the final layer and false otherwise 
                      (affects activation and batchnorm)
        '''
        if not final_layer:
            return nn.Sequential(
                nn.Conv2d(input_channels, output_channels, kernel_size, stride),
                nn.BatchNorm2d(output_channels),
                nn.LeakyReLU(0.2, inplace=True),
            )
        else:
            return nn.Sequential(
                nn.Conv2d(input_channels, output_channels, kernel_size, stride),
            )

    def forward(self, image):
        '''
        Function for completing a forward pass of the discriminator: Given an image tensor, 
        returns a 1-dimension tensor representing fake/real.
        Parameters:
            image: a flattened image tensor with dimension (im_chan)
        '''
        disc_pred = self.disc(image)
        return disc_pred.view(len(disc_pred), -1)

