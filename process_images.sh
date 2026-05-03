#!/bin/bash
cd assets
for f in ROBO-SAW*.jpg; do
  if [[ "$f" == *"alku k1"* ]]; then
    out="robosaw_kehitys_1.webp"
  elif [[ "$f" == *"alku k2"* ]]; then
    out="robosaw_kehitys_2.webp"
  elif [[ "$f" == *"alku k3"* ]]; then
    out="robosaw_kehitys_3.webp"
  elif [[ "$f" == *"piirustus"* ]]; then
    out="robosaw_piirustus.webp"
  elif [[ "$f" == *"tulostettuna"* ]]; then
    out="robosaw_tulostus.webp"
  elif [[ "$f" == *"testauksessa k1"* ]]; then
    out="robosaw_testaus_1.webp"
  elif [[ "$f" == *"testauksessa k2"* ]]; then
    out="robosaw_testaus_2.webp"
  else
    out="robosaw_extra.webp"
  fi
  echo "Processing $f -> $out"
  magick "$f" -gravity South -chop 0x250 -resize 1920x\> -quality 80 "$out"
done
rm ROBO-SAW*.jpg
