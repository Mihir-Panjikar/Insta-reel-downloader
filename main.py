import uvicorn
from fastapi import FastAPI, status, HTTPException
from instaloader.instaloader import Instaloader
from instaloader.structures import Post

app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def home(reel_url: str):
    reel = Instaloader()

    try:
        post = Post.from_shortcode(reel.context, reel_url.split("/")[-2])
        reel.download_post(post, target='reels')

        print("Reel downloaded successfully.")

    except Exception as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")
    
    return HTTPException(status_code=status.HTTP_200_OK, detail="Reel successfully downloaded")


if __name__ == "__main__":
    uvicorn.run(app)