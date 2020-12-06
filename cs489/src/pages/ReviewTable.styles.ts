import styled from "styled-components";
import matrix_img from "../assets/matrix_back_extended.jpg";

export const MainContainer = styled.div`
  background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
    url(${matrix_img});
  background-color: #ffffff;

  height: 340vh;
  display: flex;
  flex-direction: column;
  align-items: center;

  background-size: cover;
  background-repeat: no-repeat;
  background-attachment: scroll;
  -webkit-background-size: cover;
  -moz-background-size: cover;
`;
