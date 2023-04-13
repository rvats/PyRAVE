def plot_sine_1D(amp,wavelength,phase):
    x = np.arange(-500, 501, 1)
    y = np.sin((2 * np.pi * x / wavelength)+phase)
    plt.plot(x, y)
    plt.show()
plot_sine_1D(1,300,0)

def plot_sine_2D(amp,wavelength,phase,angle):
    x = np.arange(-500, 501, 1)
    X, Y = np.meshgrid(x, x)
    wavelength = 100
    sine_2D = np.sin(
        2*np.pi*(X*np.cos(angle) + Y*np.sin(angle)) / wavelength
    )
    plt.set_cmap("gray")
    plt.imshow(sine_2D)
plot_sine_2D(1,200,0,np.pi)

def compute_fft(f):
    ft = np.fft.fft2(f)
    ft = np.fft.fftshift(ft)
    return ft

sin = plot_sine_2D(1,200,0,np.pi,False)
ft = compute_fft(sin)
plt.xlim([480,520])
plt.ylim([520,480]) 
plt.imshow(abs(ft))

sin = plot_sine_2D(1,200,0,np.pi/6,False)
ft = compute_fft(sin)
plt.xlim([480,520])
plt.ylim([520,480]) 
plt.imshow(abs(ft))

f,ax = plt.subplots(1,2,figsize=(15,20))
ax = ax.flatten()
im = cv2.imread('/kaggle/input/randomimages/pic2.jpeg',-1)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ax[0].imshow(im,cmap='gray')
ax[1].imshow(20*np.log(abs(compute_fft(im))),cmap='gray')

# Plotting image and its blurred version
f,ax = plt.subplots(1,2,figsize=(15,20))
ax = ax.flatten()
im = cv2.imread('../input/randomimages/pic1.jpeg',-1)
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
im_blur = cv2.GaussianBlur(im,(7,7), 5, 5)
ax[0].imshow(im,cmap='gray')
ax[1].imshow(im_blur,cmap='gray')


def gaussian_filter(kernel_size,img,sigma=1, muu=0):
    x, y = np.meshgrid(np.linspace(-1, 1, kernel_size),
                       np.linspace(-1, 1, kernel_size))
    dst = np.sqrt(x**2+y**2)
    normal = 1/(((2*np.pi)**0.5)*sigma)
    gauss = np.exp(-((dst-muu)**2 / (2.0 * sigma**2))) * normal
    gauss = np.pad(gauss, [(0, img.shape[0] - gauss.shape[0]), (0, img.shape[1] - gauss.shape[1])], 'constant')
    return gauss

def fft_deblur(img,kernel_size,kernel_sigma=5,factor='wiener',const=0.002):
    gauss = gaussian_filter(kernel_size,img,kernel_sigma)
    img_fft = np.fft.fft2(img)
    gauss_fft = np.fft.fft2(gauss)
    weiner_factor = 1 / (1+(const/np.abs(gauss_fft)**2))
    if factor!='wiener':
        weiner_factor = factor
    recon = img_fft/gauss_fft
    recon*=weiner_factor
    recon = np.abs(np.fft.ifft2(recon))
    return recon

recon = fft_deblur(im_blur,7,5,factor=1)
plt.subplots(figsize=(10,8))
plt.imshow(recon,cmap='gray')

noise = np.random.rand(100,100)
noise_fft = np.fft.fft2(noise)
noise_fft = np.fft.fftshift(noise_fft)
f,ax = plt.subplots(1,2,figsize=(15,20))
ax = ax.flatten()
ax[0].imshow(noise,cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(20*np.log(abs(compute_fft(noise_fft))),cmap='gray')
ax[1].set_title('Fourier Transform')

gauss = gaussian_filter(7,im,5)
gauss_fft = np.fft.fft2(gauss)
gauss_fft = np.fft.fftshift(gauss_fft)
f,ax = plt.subplots(1,2,figsize=(15,20))
ax = ax.flatten()
ax[0].imshow(gauss,cmap='gray')
ax[0].set_title('Original Image')
ax[1].imshow(np.abs(gauss_fft),cmap='gray')
ax[1].set_title('Fourier Transform')

f,ax = plt.subplots(1,2,figsize=(15,20))
recon = fft_deblur(im_blur,7,5,factor='wiener')
ax[0].imshow(im_blur,cmap='gray')
ax[1].imshow(recon)
ax[0].set_title('Blurry Image')
ax[1].set_title('Image reconstruction')
plt.show()

f,ax = plt.subplots(1,2,figsize=(15,20))
recon = fft_deblur(im_blur,7,5,factor='wiener',const=0.5)
ax[0].imshow(im_blur,cmap='gray')
ax[1].imshow(recon)
ax[0].set_title('Blurry Image')
ax[1].set_title('Image reconstruction')
plt.show()