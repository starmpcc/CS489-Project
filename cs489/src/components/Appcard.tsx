import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { Button, Image } from "react-bootstrap";
import { CloseIcon, AcrylicNails } from "../assets";
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

export function Appcard(props: { name: string }) {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <Container>
      <Button onClick={handleShow}>{props.name}</Button>

      {/* <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Modal heading</Modal.Title>
        </Modal.Header>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
        </Modal.Footer>
      </Modal> */}
      <Modal isOpen={show} style={modalStyles}>
        <ModalInner>
          <ModalHeader>
            <HeaderLeft>
              <HeaderSquare /> Features
            </HeaderLeft>
            <CloseButton src={CloseIcon} onClick={handleClose} />
          </ModalHeader>
          <Image src={AcrylicNails} width="900vw"></Image>
        </ModalInner>
      </Modal>
    </Container>
  );
}
