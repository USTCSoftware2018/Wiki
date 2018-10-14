# Team

### Members

#### Management

- Wang Hao     the leader of the team
- Zhang Hao    the manager of the team

#### Frontend

- Yi Jingwei    the group leader of frontend

- Chen Lutong   the group leader of frontend

- He Liyang    the group member of frontend

- Wang Tong   the group member of frontend

- Yu Zihao   the group member of frontend

- Gao Nan    the group member of frontend

- Peng Yixing    the group member of frontend


#### Backend

- He Jiyan    the group leader of backend
- Ma Kai  the group member of backend
- Guan Xiuxian  the group member of backend
- Zhang Bowen  the group member of backend
- Zheng Qixuan   the group member of backend

#### Wiki

- Guo Yaochi   the leader of the wiki
- Pan Jie   the group member of wiki

#### Art

- Li Wenrui   the leader of the art
- Xie Bohao   the group member of the art
- Wang Tong   the group member of the art

#### Biology

- Zhou Yitian   the leader of the biology
- Cui Meiying    the group member of the biology

#### Advisor

- Hong Jiong    Primary PI
- Liu Haiyan    Secondary PI

#### All staff

- picture

#### sponsor

- Logo



### Collaborations

#### Team USTC

==Focusing on the establishment and improvement of a synthetic biology editor this year, USTC, as potential users of our bio-editor, offered us needs and opinions in application design and homepage design. For example, they suggested adding an Graphical interface to lower user threshold in which iGEMers can complete the experiment report concerning this competition .==They also helped us with biological problems we came across, such as the biological background of ==comparative sequence== analysis.

In return, we share them with some useful ==tricks(programming techniques instead)==. And we also help them in website making and modeling, which speed their work greatly. Besides, we held the annual Science and Technology Week, which spreads synthetic biology knowledge to the public. 



### Attributions

#### Developing

We sincerely thank team **USTC-Software-2017**, who gave us much advice, and their project, **Biohub 2.0**, from which our project got helped.

We sincerely thank all free software that we use like **Vue.js**, **axios** and **webpack**. They are the foundation of our project.

#### Support

We sincerely thank our advisors--**Professor Liu Haiyan**, who helped us determine the topic of our project, and **Dr. Hong Jiong**, who gave us lots of valuable advice in basic biology during our working process.

We sincerely thank the **Western Library of USTC** for their generously providing a room of long-term use for us making great progress there.

We sincerely thank the **University of Science and Technology of China Initiative Foundation** for their sponsorship all these years.

We sincerely thank the **School of Life Sciences, USTC** for their academic support and inspiring advice on our project.

#### iGEM Foundation

We sincerely thank==**Maria Bartolini**, **Vinoo Selvarajah**, **Suzie McLellan Soloviev** and **Traci Haddock-Angelli**== for offering us help, answering our questions when we developed our project.

#### Project

- **Management**: Wang Hao and Zhang Hao.
- **Frontend**: Yi Jingwei, Chen Lutong, Xie Bohao, Wang Tong, Yu Zihao, Gao Nan and He Liyang.
- **Backend**: He Jiyan, Ma Kai, Zhang Hao, Guan Xiuxian, Zhang Bowen and Zheng Qixuan.
- **Wiki**: Guo Yaochi and Pan Jie.
- **Art**: Li Wenrui, Xie Bohao and Wang Tong.
- **Biology**: Zhou Yitian and Cui Meiying.

#### Human Practice

**Science and Technology Week Committee** provided us a chance to introduce our project and iGEM to the ==citizens==.

**Asia-Pacific iGEM Conference in Taiwan** provided ==an Asian regional platform== for teams from different countries to exchange ideas and explore synthetic biology. We made a project presentation and introduced our projects.

We sincerely thank all the ==schoolmates(students instead)== and iGEMers using our software during our development. They provided a lot of useful advice and helped us improve our project.



# Project

### Description

#### Overview

​	Our product include an editor which can help you completes high-quality lab reports quickly, and a platform to ==showcase and communicate experiment-related content==. It focuses on simplifying the writing of experimental reports and standardizing the description of the experimental process. 

​	We can reduce the burden on researchers in the completion of experimental reports. Also, we can reduce unnecessary misunderstandings during the exchange of experiments by constructing a standardized discription.

​        We developed our search engine for biobricks on the base of ==2017's project==. Our engine has ==a better command of language recognition==. It is easier for synthetic biologists to find what they need without many ==input's instructions==.Additionally, we have added many useful databases and academic websites to our search engine, so biologists could search information more quickly.

​	Meanwhile, the platform provides ==the focus of attention==, enabling researchers to get new insight into the areas they need ==faster==. Users could post issues and discuss solutions related to experiments in this community. Under our standard, experimental reports will be comprehended quickly by other researchers, and ==information exchange will be more convenient==. During a new experiment, some problems might be avoided through searching for related reports in the community, which can improve the efficiency and success rate. It integrates functions of report editor,search engine.

#### Motivation

 	 After consulting with many synthetic biology workers, we found that they would inevitably suffer from the need to spend a lot of time to complete the experimental report during the experiment. At the same time, they would be prone to problems when communicating with each other for the sake of difficulty in harmonizing standards. Therefore, there is an urgent need for a standardized language to accurately describe the experimental process, and to provide a number of practical tools such as drawing, tabulation, writing articles, etc., thereby this solves these problems. 

​      As we all know,too programmer-style search engine is very unfriendly to synthetic biologists, so we reidesigned functions of search engines.Researchers can easily find reports written by others after inputting some key words.They could also search information in some databases and websites directly though this engine.      

​       For most synthetic biology workers, it is difficult for them to conduct effective communication on experimental content, so we established a synthetic biology community based on search engine and report editor. In this community, bio workers can use this to record their experimental process and comment on other scholar's reports, thereby reducing the blindness of the research.

#### To be improved（暂缺）

The interface design of the editor is not yet fully finalized. We also need to further refine the design and implementation based on the features we want to implement. At the same time, we will add and debug more new features. The communication platform we will build will also begin testing



### Video(暂缺)



### Model（暂缺）





### Implementation

#### Server Part

The server of Bioeditor is written in Python 3.6, which is a flexible and cross-platform language and can reduce the learning costs we develop. Django allows fast prototyping and large-scale deployment, that's why we choose Django to be the basic framework.

##### About the Bricks Data(暂缺)



##### About Data Organizing

The initial data will be imported into a separate database.Bioeditor will link to it by creating virtual tables using MySQL's database view technology.Using database views may lower the speed of querying, but it also has a lot of benefits. On one hand,it's easy to get started.Users don't need to care about the complex structure behind. On the other hand,it's easy for beginners, users who use views can only access the result set they are allowed to query. 

##### About search engine

We followed last year's filtering of initial data to reduce the impact of unwanted bricks on search efficiency.We used natural language processing during the search process. After the language model is established, the extraction of text keywords is realized by processing such as statistical features such as TF and IDF. So that our search results are more in line with the needs of the user.

At the same time, we have made the search conditions more diversified.Users can find the bricks they need more conveniently under more query conditions.

We will recalculate the ranking weights at regular intervals. The reason for not evaluating them in real time is that the task may update the whole table and become time-consuming. 

#### Frontend Part

In most templating systems,any changes that the user makes to the view are not reflected in the model. This means that the developer has to write code that constantly synchronize the view with the model and the model with the view.

So we chose the Angular template, which works differently. Any changes to the view are immediately reflected in the model, and any changes in the model are propagated to the view.You can think of the view as simply an instant projection of your model.

##### About UI

We choose NG-ZORRA as our basic framework. NG-ZORRA is a UI framework developed by Alibaba Group based on Angular template.NG-ZORRA provides us with multiple elegant components and comfortable visual experience. In addition,we also added many wonderful customized conponents and styles to improve the user experience.

##### About sortable

When researchers writes an academic report,the scholar could click and drag the element of experimental process from the list to a new location in the report.Obviously,It is convenient for them to write experimental reports.





### Improve(暂缺)

NLP,deep learning



### Installation(暂缺)





# Human Practice

### Human Practice

#### Science and Technology Week

Science and Technology Week is a large-scale, centralized science popularization campaign organized by the China University of Science and Technology. This year, Science and Technology Week attracted over ten thousand citizens to USTC, varying from primary pupils, high school students and college students in biology-related majors to the public from all walks who may have limited knowledge of Synthetic Biology. Our team cooperated with Team USTC and offered visitors a feast of biological knowledge and a chance to cultivate interest in biology.

We introduced elementary knowledge of genetics to citizens by poster presentation and our explanation,  showed them some basic experiment operation, like liquid relief, centrifugation and etc.Then we educated and inspired visitors' interest by allowing them to observe biochemical-related sections under a laboratory microscope. In addition, we distributed questionnaires to visitors to get their feedback on synthetic biology to improve our design of our software.

### Integrated Human Practice

#### Student Open Source Conference

The Student Open Source Annual Meeting was the first open source technology summit in China that was organized by student organizations. The main theme of the conference is understand, participate in, and contribute to open source. Our team signed up for this annual meeting.And at the meeting, our team leader and a team member worked together to complete the report on our iGEM project. We introduced the iGEM competition and the synthetic biology to the audience.At the same time, we also introduced the positive significance of our project to synthetic biology to the audience. We received useful feedbacks and technology-improvement suggestions from audience.

#### Asia-Pacific Conference in Taiwan

We attended International Genetically Engineered Machine Conference held by National Chung Hsing University from July 30th to August 3rd 2018. Over 20 iGEM teams attended the conference and 5 members of our team was sent to Taiwan.

During the conference, the iGEMers communicated, exchanged ideas and learned from one another. The conference is not only a simple warm-up for the upcoming world championship in Boston, but an Asian regional platform for teams from different countries to exchange ideas and explore synthetic biology as well. All the teams made a project presentation and introduced their projects. In this way, we received useful feedbacks and technology-improvement suggestions from students and professors of other teams.



# Requirements

### Contribution

Bioeditor is designed for synthetic biologists, focusing on completing standardized experimental reports quickly and accurately. It is also a versatile software to meet the needs of synthetic biologists. It reduces the barriers of synthetic biologists in the communication process.
Please visit Description for more details about our project and what we have achieved.