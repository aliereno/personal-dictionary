# Personal Dictionary system with Flask-SQLAlchemy

### Installation & Run:

* This project uses [WordsAPI](https://www.wordsapi.com/), so `X-RAPIDAPI-KEY` must be set in .env file.

After the .env editing, simply run;

```
flask run

# or if you use docker
docker-compose up
```

For the migrations;

```
flask db upgrade
```

###

### System Preview

<img src="/gifs/system_recording.gif" width="1200" height="500" alt="system recording"/>

### Projects Structure

<img src="/gifs/project_structure.gif" width="800" height="700" alt="project structure"/>

### Features

| Feature |  
| ------ | 
| Repository Service Pattern |
| Docker |
| Boostrap |
| Log Tracing |
| Env support |
| Metric Monitoring |