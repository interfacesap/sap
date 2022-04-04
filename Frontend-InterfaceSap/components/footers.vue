<template>
    <footer class="rodape">
      <h4>© Robert Bosch Ltda. 2022, all rights reserved</h4>
    </footer>
</template>

<style lang="scss" scoped>
@import "@/layouts/variaveis.scss";

.rodape {
  height: $alturaFooter;
  width: 100vw;
  box-shadow: 0px -3px 10px 2px #b8b7b7;
  margin: 0;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  h4{   
    margin-left: 2%;
    font-size: 12px;
 }
}

</style>