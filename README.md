დაბილდვა

git clone https://github.com/skt7tks/monitoring_project.git
cd monitoring_project
docker-compose up --build -d
ipconfig

# Python Prometheus Exporter + Prometheus + Grafana

## აღწერა

ეს პროექტი აერთიანებს Python-ში დაწერილ მარტივ Exporter-ს, რომელიც ცვლის HTTP რეაგირების დრო და სტატუს კოდს Prometheus-ისთვის. ასევე შედის Prometheus მონიტორინგის და Grafana ვიზუალიზაციის სერვისები.

---

## ფაილები

- `requirements.txt` - Python ბიბლიოთეკების ჩამონათვალი  
- `Dockerfile` - Docker იმიჯის შესაქმნელად Python აპლიკაციისთვის  
- `exporter.py` - Python აპლიკაციის მთავარი კოდი  
- `prometheus/prometheus.yml` - Prometheus-ის კონფიგურაცია  
- `docker-compose.yml` - Docker Compose კონფიგურაცია ყველა სერვისისთვის  

---

## მოთხოვნები

- Docker  
- Docker Compose  

---

## გამოყენების ინსტრუქცია

1. დააინსტალირე Docker და Docker Compose.  
2. პროექტის ფოლდერში (სადაც არის `docker-compose.yml`) გაუშვი:  
   ```bash
   docker-compose up --build

