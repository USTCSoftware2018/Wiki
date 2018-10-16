# Project

## Description

### Overview

### What is BioHub 3.0?

BioHub 3.0 is a synthetic biology community, integrated **Intelligent Search Engine** and the online report **editor**. It brings you a new way to edit your reports and search whatever you need only in one step.

#### The Editor

We established a standardized description of experimental steps. The editor can help you complete high-quality lab reports quickly just by choosing steps and filling in the blanks. Custom steps and protocols are also supported. And in our report editor, biologists could use a number of practical tools such as drawing, tabulation and writing articles, which improve the efficiency of completing the experiment report.

#### Intelligent Search Engine

We developed our search engine on the base of 2017's project. Our engine has a better command of language recognition. It supports **semantic recognition**, like "reports today", "reports by ana", "reports this year" and etc. Meanwhile, we listened to the opinions of the judges. This year we added **advanced search** and we can now sort the results by time, labels, etc.. It is easier for synthetic biologists to find what they need without many input's instructions. Additionally, we have added many useful databases and academic websites to our search engine, so biologists could search information more quickly.

#### The community

In this community, bio workers can record their experimental process and release those reports. Meanwhile, they could also read and comment on other scholar's reports. In this way, we make the academic discussion more convenient.  We provide both site search and off-site search to provide a better user experience.

### Motivation

After consulting with several synthetic biology workers, we found that they would inevitably suffer from the need to spend a lot of time to complete the experimental report during the experiment. Therefore, there is an urgent need for an editor that provides a number of practical tools such as drawing, tabulation, writing articles by dragging steps or protocols to improve efficiency. So it can replace the original Pages or Microsoft Office for its convenience.

As we all know, a too programmer-style search engine is very unfriendly to synthetic biologists, so we redesigned functions of search engines. Researchers can easily find reports written by others after inputting some keywords. They could also search information in some databases and websites directly through this engine.      

 For most synthetic biology workers, it is difficult for them to conduct effective communication on experimental content, so we established a synthetic biology community based on search engine and report editor. In this community, bio workers can use this to record their experimental process and comment on other scholar's reports, thereby reducing the blindness of the research.



#### To be improved（暂缺）

The interface design of the editor is not yet fully finalized. We also need to further refine the design and implementation based on the features we want to implement. At the same time, we will add and debug more new features. The communication platform we will build will also begin testing.



### Video(暂缺)



### Model（暂缺）





### Implementation

#### Server Part

The server of Bioeditor is written in Python 3.6, which is a flexible and cross-platform language and can reduce the learning costs we develop. Django allows fast prototyping and large-scale deployment, that's why we choose Django to be the basic framework.

##### About the Bricks Data(暂缺)



##### About Data Organizing

The initial data will be imported into a separate database. Bioeditor will link to it by creating virtual tables using MySQL's database view technology. Using database views may lower the speed of querying, but it also has a lot of benefits. On one hand, it's easy to get started. Users don't need to care about the complex structure behind. On the other hand, it's easy for beginners, users who use views can only access the result set they are allowed to query. 

##### About search engine

We followed last year's filtering of initial data to reduce the impact of unwanted bricks on search efficiency.We used natural language processing during the search process. After the language model is established, the extraction of text keywords is realized by processing such as statistical features such as TF and IDF. So that our search results are more in line with the needs of the user.

At the same time, we have made the search conditions more diversified. Users can find the bricks they need more conveniently under more query conditions.

We will recalculate the ranking weights at regular intervals. The reason for not evaluating them in real time is that the task may update the whole table and become time-consuming. 

#### Frontend Part

In most templating systems, any changes that the user makes to the view are not reflected in the model. This means that the developer has to write code that constantly synchronize the view with the model and the model with the view.

So we chose the Angular template, which works differently. Any changes to the view are immediately reflected in the model, and any changes in the model are propagated to the view. You can think of the view as simply an instant projection of your model.

##### About UI

We choose NG-ZORRA as our basic framework. NG-ZORRA is a UI framework developed by Alibaba Group based on Angular template.NG-ZORRA provides us with multiple elegant components and comfortable visual experience. In addition, we also added many wonderful customized components and styles to improve the user experience.

##### About sortable

When a researcher writes an academic report, he/she could click and drag the element of the experimental process from the list to a new location in the report. Obviously, it is convenient for them to write experimental reports.





### Improve(暂缺)

NLP, deep learning



### Installation(暂缺)
