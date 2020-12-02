import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button, Image } from "react-bootstrap";
import { CloseIcon } from "../assets";
import {
  Container,
  modalStyles,
  ModalHeader,
  ModalInner,
  HeaderLeft,
  HeaderSquare,
  CloseButton,
} from "./Appcard.styles";
import "../styles/css/Reviewcard.css";
import Modal from "react-modal";

export function Appcard(props: { name: string; img: any }) {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <Container>
      <Button onClick={handleShow}>{props.name}</Button>
      <Modal isOpen={show} style={modalStyles}>
        <ModalInner>
          <ModalHeader>
            <HeaderLeft>
              <HeaderSquare /> Features
            </HeaderLeft>
            <CloseButton src={CloseIcon} onClick={handleClose} />
          </ModalHeader>
          <Image src={props.img} width="900vw"></Image>
        </ModalInner>
      </Modal>
    </Container>
  );
}
