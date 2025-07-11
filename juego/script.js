const html = document.querySelector("html")
const canvas = document.querySelector("canvas")
const ctx = canvas.getContext('2d', { willReadFrequently: true });

class Player {
    constructor() {
        this.x = 0
        this.y = 0

        this.vx = 0
        this.vy = 0
        this.gravity = 0.5
        this.jumpForce = -10
        this.onGround = false

        this.playerSize = canvas.width / 15
        this.speed = 2

        document.addEventListener("keydown", (e) => {
            if (e.key === "ArrowLeft") this.vx = -this.speed
            if (e.key === "ArrowRight") this.vx = this.speed
            if (e.key === " " && this.onGround) {
                this.vy = this.jumpForce
                this.onGround = false
            }
        })

        document.addEventListener("keyup", (e) => {
            if (e.key === "ArrowLeft" || e.key === "ArrowRight") this.vx = 0
        })
    }

    collide(x, y) {
        let pixelColor = ctx.getImageData(x, y, 1, 1).data
        return pixelColor[3] !== 255 // true si se puede pasar
    }

    update() {
        // Gravedad
        this.vy += this.gravity

        // Movimiento horizontal
        if (
            this.vx < 0 &&
            this.collide(this.x - 1, this.y) &&
            this.collide(this.x - 1, this.y + this.playerSize - 1)
        ) {
            this.x += this.vx
        } else if (
            this.vx > 0 &&
            this.collide(this.x + this.playerSize, this.y) &&
            this.collide(this.x + this.playerSize, this.y + this.playerSize - 1)
        ) {
            this.x += this.vx
        }

        // Movimiento vertical
        this.y += this.vy

        // Colisión con suelo (parte inferior del canvas)
        if (this.y + this.playerSize >= canvas.height) {
            this.y = canvas.height - this.playerSize
            this.vy = 0
            this.onGround = true
        } else {
            // Verifica si está tocando suelo (pixel sólido debajo)
            let belowLeft = ctx.getImageData(this.x + 1, this.y + this.playerSize, 1, 1).data[3]
            let belowRight = ctx.getImageData(this.x + this.playerSize - 1, this.y + this.playerSize, 1, 1).data[3]
            if (belowLeft === 255 || belowRight === 255) {
                this.y = Math.floor(this.y / this.playerSize) * this.playerSize
                this.vy = 0
                this.onGround = true
            } else {
                this.onGround = false
            }
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

    player.update()
    player.draw()

    requestAnimationFrame(update)
}

background.onload = () => {
    ctx.imageSmoothingEnabled = false

    // Zoom comentado
    // if (html.clientWidth < 700) {
    //     canvas.style.zoom = Math.floor(html.clientWidth / canvas.width)
    // } else {
    //     canvas.style.zoom = Math.floor(html.clientWidth / canvas.width) / 2
    // }

    player = new Player()

    requestAnimationFrame(update)
}
