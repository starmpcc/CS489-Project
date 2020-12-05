import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container, Title } from "./Home.styles";
import { Appcard } from "../components/Appcard";

import { reviewdata } from "../utils/data";

import "./TestPage.css";

import {
  img1,
  img2,
  img3,
  img4,
  img5,
  img6,
  img7,
  img8,
  img9,
  img10,
  img11,
  img12,
  img13,
  img14,
  img15,
  img16,
  img17,
  img18,
  img19,
  img20,
} from "../assets";

export function Reviewtable() {
  const [imagename, setImagename] = useState("");

  function filter(name: string) {
    if (name == "AcrylicNails") return img1;
    else if (name == "BallFitPuzzle") return img2;
    else if (name == "Car Destruction") return img3;
    else if (name == "Carve The Pencil") return img4;
    else if (name == "Cornhole League") return img5;
    else if (name == "Dragonscapes Adventure") return img6;
    else if (name == "Dropping Ball2") return img7;
    else if (name == "Face Clinic") return img8;
    else if (name == "Fruit Ninja 2 - Func Action Games") return img9;
    else if (name == "God Of Pranks") return img10;
    else if (name == "Hero VS Criminal") return img11;
    else if (name == "Idlemon Tales") return img12;
    else if (name == "Legends of Idleon -- Idle MMO") return img13;
    else if (name == "Lucky drop - Monster drop") return img14;
    else if (name == "Restaurant Life") return img15;
    else if (name == "Roof Rails") return img16;
    else if (name == "Save Daddy - Pull the Pin Game") return img17;
    else if (name == "Save them all - drawing puzzle") return img18;
    else if (name == "Stretch Guy") return img19;
    else if (name == "Warpath") return img20;
  }

  return (
    <Container>
      <label>
        <Container>
          <Title>Review Alert</Title>
        </Container>
        {reviewdata.map((item) => (
          <Appcard name={item.Name[0]} img={filter(item.Name[0])} />
        ))}
      </label>
    </Container>
  );
}
