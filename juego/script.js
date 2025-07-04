const html = document.querySelector("html")
const canvas = document.querySelector("canvas")
const ctx = canvas.getContext('2d', { willReadFrequently: true });

class Player {
    constructor() {
        this.x = 0
        this.y = 0

        this.playerSize = canvas.width/15

        this.isMoving = false

        document.addEventListener("keydown", (e) => {
            if (!this.isMoving) {
                this.isMoving = true
                this.interval = setInterval(() => {
                    this.move(e)
                }, 10)
            }
        })
        
        document.addEventListener("keyup", () => {
            clearInterval(this.interval)
            this.isMoving = false
        })
    }

    collide(x, y) {
        let pixelColor = ctx.getImageData(x, y, 1, 1).data
        if (pixelColor[3] == 255) return false
        else return true
    }

    move(e) {
        switch (e.key) {
            case "ArrowLeft":
                if (this.collide(this.x-1, this.y) && this.collide(this.x-1, this.y + this.playerSize - 1)) {
                    this.x-=2
                }
                break
            case "ArrowRight":
                if (this.collide(this.x + this.playerSize, this.y) && this.collide(this.x + this.playerSize, this.y + this.playerSize - 1)) {
                    this.x+=2
                }
                break
            case "ArrowUp":
                if (this.collide(this.x, this.y-1) && this.collide(this.x + this.playerSize - 1, this.y-1)) {
                    this.y-=2
                }
                break
            case "ArrowDown":
                if ((this.collide(this.x, this.y + this.playerSize)) && this.collide(this.x + this.playerSize - 1, this.y + this.playerSize)) {
                    this.y+=2
                }
                break
        }
    }
    draw() {
        ctx.fillRect(this.x, this.y, this.playerSize, this.playerSize)
    }
}

const background = new Image()
background.src = "./background/level0.png"

function update() {
    ctx.clearRect(0, 0, canvas.width, canvas.height)

    ctx.drawImage(background, 0, 0, canvas.width, canvas.height)

    player.draw()
    
    requestAnimationFrame(update)
}

background.onload = () => {
    ctx.imageSmoothingEnabled = false

    // console.log((html.clientWidth / canvas.width))
    // if (html.clientWidth < 700) {
    //     canvas.style.zoom = Math.floor(html.clientWidth / canvas.width)
    // }
    // else {
    //     canvas.style.zoom = Math.floor(html.clientWidth / canvas.width) / 2
    // }

    player = new Player()

    requestAnimationFrame(update)
}