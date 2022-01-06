import uvicorn

# run fastapi

apps = ["d001-s1", "d001-s1", "log"]  # can add more apps if needed

if __name__ == "__main__":
    print("Pick api to run by typing a number starting at 0 corresponding to list below")
    print(apps)
    x = input()
    y = apps[int(x)]


    uvicorn.run(y+":app", host="127.0.0.1", port=5000, log_level="info")


# goto http://127.0.0.1:5000/docs
