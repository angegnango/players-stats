# Docker Flask 

Service built in top of [Docker Compose](https://docs.docker.com/compose/) template for orchestrating a [Flask](http://flask.pocoo.org/) application & a 

### Installation

```bash
git clone https://github.com/angegnango/players-stats-tdd
```

### Build & Launch

```bash
docker-compose up
```

This will expose the Flask application's endpoints on port `http://YourIp:3000` 

get the IP from docker console


### Endpoints
---

![API Documentation](swagger.png)

### How to use
---

Get a token
![API Documentation](token.png)

Add a player
![API Documentation](addPlayer.png)

Get player stat
![API Documentation](playerStats.png)



To shut down:

```bash
docker-compose down
```



---