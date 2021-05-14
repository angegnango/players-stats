from api.server import init_server
app = init_server()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)