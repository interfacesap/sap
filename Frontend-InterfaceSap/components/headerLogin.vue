<template>
  <div>
      <div class="line"></div>
      <header class="menu">
        <section class="imagem_logo"></section>
        <section class="meio_header"></section>
      </header>
  </div>
</template>

<style lang="scss" scoped>
@import "@/layouts/variaveis.scss";
$image: "@/static/logo.png";

 .menu {
  height: calc($alturaHeader - $alturaLine);
  width: 100vw;
  display: flex;
  flex-direction: row;
}

.meio_header {
  height: 100%;
  width:calc(100vw - 15%);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  background-color: white;
}

.line {
  margin-top: 0;
  height: $alturaLine;
  background-image: url('/linha.jfif');
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: center;
}

.imagem_logo {
  height: 100%;
  width: 15%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background-color: white;
  background-image: url($image);
  background-size: contain;
  background-repeat: no-repeat;
  background-position: center;
}

@media screen and (max-width: 500px) {
  .imagem_logo{
  height: 100%;
  width: 25%;
  margin-left: 4px;

  }

}


</style>
