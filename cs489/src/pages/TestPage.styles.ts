import styled from "styled-components";
import matrix_img from "../assets/matrix_back.jpg";

export const Container = styled.div`
  width: 1100px;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0 auto;

  justify-content: center;
`;

export const Section = styled.div`
  margin-top: 30px;
  width: 50%;
`;

export const SectionTitle = styled.div`
  font-size: 20px;
  font-weight: bold;
  margin-bottom: 10px;
`;

export const TextArea = styled.textarea`
  min-height: 300px;
  width: 100%;
`;

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
