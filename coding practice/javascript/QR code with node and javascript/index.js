
//these are the required modules we'll need
import inquirer from "inquirer";
import fs from "fs";
import * as qr from "qr-image";


inquirer
    .prompt([
        {
            type: 'input', //type of string the user will give
            name: 'url', //name of the user's input
            message: "input an URL: " //message to tell the user what to input
        },    
    ])

    .then((answer) => {
        //save what url the png take you to in a txt file
        fs.writeFile("input.txt", `${answer['url']}\n`, 'utf8', (err) => {
            console.log('done')
        })

        //variable we'll need to make the url into a qr code png
        var qr_svg = qr.image(answer['url'], { type: 'png' });  //makes a readable stream with image data
        //creates the png file
        qr_svg.pipe(fs.createWriteStream(`qr_code.png`)); //creates the png file
    })

    .catch((error) => {
        console.error("Error: ", error)
    })