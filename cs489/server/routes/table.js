const express = require("express");
const router = express.Router();
const cors = require("cors");

router.get("/:id", (req, res) => {
  let name = req.params.id;
  console.log("call table for", name);
  //////////////////////////////////////////////////////////
  let score = 0;

  ///////////////////////////////////////////////////////////

  res.send({ score: score });
});

module.exports = router;
