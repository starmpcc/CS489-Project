import React from "react";
import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import { Button } from "react-bootstrap";
import { Container } from "./Home.styles";
import { Appcard } from "../components/Appcard";

import "./TestPage.css";

export function Reviewtable() {
  const data = [{ name: "tttt" }, { name: "sss" }];

  return (
    <Container>
      <label>
        <Container>
          <h2>게임 리뷰들입니다</h2>
        </Container>
        {data.map((item) => (
          <Appcard name={item.name} />
        ))}
      </label>
    </Container>
  );
}
