import styled, { css } from "styled-components";

export const Container = styled.div`
  padding-top: 10px;
  padding-bottom: 10px;
  display: flex;
  flex-direction: column;
  max-width: 1100px;
  align-self: center;
  align-items: center;
`;

export const modalStyles = {
  content: {
    top: "50%",
    left: "50%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
  },
  overlay: {
    background: "rgba(0,0,0,0.5)",
  },
};

export const ModalInner = styled.div`
  width: 900px;
  height: 460px;
  background-color: white;
  border-radius: 5px;
  padding: 45px 90px;
`;

export const ModalHeader = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 40px;
`;

export const HeaderLeft = styled.div`
  display: flex;
  align-items: center;
  font-size: 36px;
  font-weight: bold;
`;

export const HeaderSquare = styled.div`
  width: 37px;
  height: 37px;
  background: #3d0089;
  margin-right: 6px;
`;

export const CloseButton = styled.img`
  width: 26px;
  height: 26px;
  cursor: pointer;
`;

export const WidenButton = styled.button`
  width: 100%;
  height: 50px;
  font-size: 30px;
  font-weight: bold;
  margin: 30px 0;
  background-color: #007fff;
  color: white;
  border: none;
  cursor: pointer;
`;
