---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
marp: true
backgroundImage: file('./AA_Logo.jpg')
---

![bg left:20% 80%](./AA_Logo.jpg)

# **Creating alerts programatically in Databricks**

_Presenter_ : 

Vasileios (Vasilis) Anagnostopoulos

---

![bg left:20% 80%](./AA_Logo.jpg)

# What we will discuss

* What are Databricks alerts
* How to create an alert manually
* How to create an alert programatically
* Manually?
* Programatically

---

![bg left:20% 80%](./AA_Logo.jpg)

# What are Databricks alerts

1. Dynamic datasets may change in interesting ways
2. Databricks alerts are a way of monitoring and notifying about interesting changes.
3. It is implemented as an SQL query that returns a true or false flag a.k.a. condition
4. It is a databricks native solution
5. Could be implemented by Airflow

---

![bg left:20% 80%](./AA_Logo.jpg)

# How to create an alert manually

**Demo time**

---

![bg left:20% 80%](./AA_Logo.jpg)

# How to create an alert programatically

**Demo time**

---

![bg left:20% 80%](./AA_Logo.jpg)

# Manually?

1. Manual is easy but requires co-ordination.
2. Manual hides resources, programmatic offers explicit resource management.
3. Manual needs UI, cannot be automated.

---

![bg left:20% 80%](./AA_Logo.jpg)

# Programatically?


1. Programmatic can be version controlled and have some unit tests.
2. Programmatic can run automatically in CD pipeline.
3. Programmatic can be centralized through service principal.