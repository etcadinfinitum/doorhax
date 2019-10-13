# doorhax
Front-end for DubHacks 2019 project with @udomugo, @mkhsu, and @cforcomputer

## DOORS
(Directed Open Object Reality Simulator)

## Inspiration
We were inspired by a demo that we saw where someone created a model of a tardis that made it appear bigger on the inside using AR technology. We started to think about how we could apply this technique on a larger scale, and the potential community health benefits it could provide. 

## Overview
Doors is a software application used for detecting apertures such as windows and doorways in static environments. After detecting a doorway, object persistence maintains the positions of the “doors” and replaces them with a simulated environment.

## What it does
The objective of DOORS is to blend reality with a layer of virtual reality. The virtual reality layer causes the room, or multiple rooms -  to become separated and/or isolated from the broader world. This simulated isolation can be blended with modern passthrough VR or AR headsets, along with future headset technologies. 

Our hypothesis is that this simulated isolation can help individuals with autism, ADHD, and related focus/anxiety disorders. This application is of particular interest to those who have difficulty adjusting to new environments. By making it so that they always feel that their current environment is surrounded by their familiar virtual environment, DOORS users feel safe and comfortable in unfamiliar environments.

## How we built it
For the purpose of Dubhacks 2019, we’ve created an interactive demonstration in the form of a web application. The web application is running a Flask frontend with a Google Cloud backend. Static images are fed in to the Google Cloud backend, which takes them and replaces the empty space in doors using a machine vision algorithm trained on images of doors. The output is then displayed in the browser for the purposes of our demonstration.

## The Future
We could see DOORS being used for various therapy purposes. By adding a layer of familiar unreality, they may feel more open to engage with a therapist. DOORS could also be used to simulate different times of day through windows, allowing for “real life desktop backgrounds”. For those who have to deal with odd schedules, DOORS could be used to help maintain circidian rhythm and simultaniously fight depression in areas of the world that get low sunlight exposure. 
