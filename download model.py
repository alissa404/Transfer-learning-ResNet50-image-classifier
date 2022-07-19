# downloading ResNet50 in Keras generates "SSL: CERTIFICATE_VERIFY_FAILED"
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# fetch online pretrained model
model = ResNet50(weights='imagenet')