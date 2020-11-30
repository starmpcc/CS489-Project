import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container } from "./Home.styles";
import { Appcard } from "../components/Appcard";

import { reviewdata } from "../utils/data";

import "./TestPage.css";

export function Reviewtable() {
  return (
    <Container>
      <label>
        <Container>
          <h2>게임 리뷰들입니다</h2>
        </Container>
        {reviewdata.map((item) => (
          <Appcard name={item.Name[0]} />
        ))}
      </label>
    </Container>
  );
}
