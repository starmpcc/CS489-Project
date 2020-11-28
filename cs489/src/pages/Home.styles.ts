import styled from "styled-components";
import { Button } from "react-bootstrap";
import matrix_img from "../assets/matrix.png";

export const MainContainer = styled.div`
  background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
    url(${matrix_img});
  background-color: #ffffff;

  height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;

  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: scroll;
  -webkit-background-size: cover;
  -moz-background-size: cover;
`;

export const Container = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`;

export const LoadingText = styled.h1`
  color: white;
`;
