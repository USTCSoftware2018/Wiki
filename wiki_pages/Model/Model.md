# Model

There're two outstanding models supporting our project:

- **Natural language processing (NLP)** 
- **Object-relational mapping (ORM)**

## **Natural language processing (NLP)** 

Natural language processing (NLP) is an area of computer science and artificial intelligence that is concerned with the interaction between computers and humans in natural language.

The ultimate goal of NLP is to enable computers to understand language as well as we do.

For example, we can use these keywords to search:

```
molecular biology
```

But NLP give us the power to get closer to what we actually want to search:

```
molecular biology by Someone this year with #immunity
```

NLP can extract all the information and construct a query action:

```
keyword: molecular biology
author: Someone
time: this year
label: #immunity
```

In our project, we use an open-source software named **Stanford CoreNLP** (https://stanfordnlp.github.io/CoreNLP/) to parse the search string.

![image-20181017181227081](image-20181017181227081.png)

CoreNLP provides many underlying models so that we can get analysis information to construct more expressive and more human-friendly query.

## **Object-relational mapping (ORM)**

Object-Relational Mapping (ORM) allows us to work with objects and have them saved to the database automatically. It can greatly simplify create-read-update-delete (CRUD) operations and make our code more comprehensive.

ORM makes our `user`,`report`,`notice` and more models easy to query, to list and to link to each other.

In our project, we use **Django ORM** with MySQL backend as the underlying models to provide fast and flexible queries.
