# Data Augmentation
![](https://github.com/Mrfrktmrck19/Data_Science/blob/master/Images/DataAugmentation.png)
## What is Data Augmentation
Data Augmentation is set of techniques to artifically increace the amount of data bt generating new data points from existing data.   <br/>
This includes making small changes to data or using deep learning models to generate new data points. <br/>
##  Why Should we use these techniques?
Machine learning application especially in the deep learning domain continue to diversify and increase rapidly. Data Augmentation techniques may be a good <br/>
tool againist to challanges which artifical intelligence world faces.
Data Augmentation is useful to improve performance and outcomes of machine learning models by forming new and different examples to train datasets. If the dataset in a machine learning model is rich and sufficient, the model performs better and more accurately. <br/>
For machine learning models, collecting and labelling of data can be exhausting and costly processes. Transformations in datasets by using data augmentation techniques allow companies to reduce these operational costs.    <br/>
One of the steps into a data model is cleaning data which is necessary for high accuracy models. However, if cleaning reduces the representability of data, then the model cannot provide good predictions for real world inputs. Data augmentation techniques enable machine learning models to be more robust by creating variations that the model may see in the real world.      <br/> <br/>
##  How does it work?
![](https://github.com/Mrfrktmrck19/Data_Science/blob/master/Images/dataAug2.png) <br>
*For image classification and segmentation*   <br/>
For data augmentation, making simple alterations on visual data is popular. In addition, generative adversarial networks (GANs) are used to create new synthetic data. Classic image processing activities for data augmentation are:
 - padding
 - random rotating
 - re-scaling,
 - vertical and horizontal flipping
 - translation ( image is moved along X, Y direction)
 - cropping
 - zooming
 - darkening & brightening/color modification
 - grayscaling
 - changing contrast
 - adding noise
 - random erasing

<br/><br/><br/>
![](https://github.com/Mrfrktmrck19/Data_Science/blob/master/Images/dataAug3.png)

<br/><br/><br/>
Advanced models for data augmentation are

_Adversarial training/Adversarial machine learning:_ It generates adversarial examples which disrupt a machine learning model and injects them into a dataset to train.
<br>
_Generative adversarial networks (GANs):_ GAN algorithms can learn patterns from input datasets and automatically create new examples which resemble training data.
<br>
_Neural style transfer:_ Neural style transfer models can blend content image and style image and separate style from content.
<br>
_Reinforcement learning:_ Reinforcement learning models train software agents to attain their goals and make decisions in a virtual environment.

Popular open source python packages for data augmentation in computer vision are Keras ImageDataGenerator, Skimage and OpeCV.
<br><br>

**For natural language processing (NLP)**       <br>
Data augmentation is not as popular in the NLP domain as in the computer vision domain. Augmenting text data is difficult, due to the complexity of a language. Common methods for data augmentation in NLP are:  <br><br>

 - Easy Data Augmentation (EDA) operations: synonym replacement, word insertion, word swap and word deletion
 - Back translation: re-translating text from the target language back to its original language
 - Contextualized word embeddings

<br><br>
## What are the benefits of data augmentation?
 - Improving model prediction accuracy
   - adding more training data into the models
   - preventing data scarcity for better models
   - reducing data overfitting  and creating variability in data
   - increasing generalization ability of the models
   - helping resolve class imbalance issues in classification
 - Reducing costs of collecting and labeling data
 - Enables rare event prediction
 - Prevents data privacy problems


Source: https://research.aimultiple.com/data-augmentation/#:~:text=Data%20augmentation%20is%20a%20set,to%20generate%20new%20data%20points.
