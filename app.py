from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<animals>")
def animal_page(animals):
    data = {}
    if animals == "dogs":
        data = {
            "Bulldog": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://www.thesprucepets.com/thmb/FEsGt1xpqpRi_YzoMCuzPEWcvso=/872x654/smart/filters:no_upscale()/1024px-Bulldog_inglese-cf544d354159462c8c0d93db5f1adbe6.jpg"
            },
            "Labrador Retriever": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F06%2F25%2Flabrador-retriever-yellow-sitting-275580695-2000.jpg"
            },
            "German Shepherd": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://highlandcanine.com/wp-content/uploads/2020/12/iStock-926735822.jpg"
            }
        }
    elif animals == "cats":
        data = {
            "Persian Cat": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://vetstreet.brightspotcdn.com/dims4/default/5c40e17/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2F51%2F45%2Fa7f47de448fabce6e4a908cb878d%2FPersian-AP-J6XREO-645sm3614.jpg"
            },
            "Bengal Cat": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://imagesvc.meredithcorp.io/v3/mm/image?url=https%3A%2F%2Fstatic.onecms.io%2Fwp-content%2Fuploads%2Fsites%2F47%2F2021%2F04%2F20%2Fbengal-wood-walking-867775498-2000.jpg"
            },
            "Scottish Fold": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://media.istockphoto.com/photos/scottish-fold-shorthair-cat-resting-on-chair-picture-id468382096?k=20&m=468382096&s=612x612&w=0&h=RsTfL4E3kj0n0XoP_gVAduS549Aev5dJcklBMkZA49I="
            }
        }
    elif animals == "horses":
        data = {
            "Arabian horse": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://upload.wikimedia.org/wikipedia/commons/5/54/Halterstandingshotarabianone.jpg"
            },
            "Thoroughbred": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://animals.net/wp-content/uploads/2020/03/Thoroughbred-7-650x425.jpg"
            },
            "American Quarter Horse": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://upload.wikimedia.org/wikipedia/commons/9/9d/Quarter_Horse%28REFON%29-cleaned.jpg"
            }
        }
    elif animals == "rabbits":
        data = {
            "Holland Lop": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://www.petguide.com/wp-content/uploads/2016/06/holland-lop.jpg"
            },
            "Netherland Dwarf Rabbit": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://petkeen.com/wp-content/uploads/2020/10/Brown-Netherland-dwarf-rabbit_RATT_ANARACH_Shutterstock.jpg"
            },
            "European Rabbit": {
                "price": "$100",
                "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Sint, pariatur.",
                "image_url": r"https://lafeber.com/vet/wp-content/uploads/european-rabbit.jpg"
            }
        }
    
    return render_template("animal.html", animals=animals.capitalize(), data=data)


if __name__ == "__main__":
    app.run(debug=True)
