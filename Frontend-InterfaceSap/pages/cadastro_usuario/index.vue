// Cadastro Usuario 

<template>
  <div class="cont">
    <headers/>
    <div class="principal">
      <div class="base">
        <h1>Cadastro Usuario</h1>
        <input type="text" name="usuario" class="inputs" id="input1" placeholder="Usuario">
        <input type="text" name="nome" class="inputs" id="input2" placeholder="Nome">
        <input type="email" name="email" class="inputs" id="input3" placeholder="email">
        <input type="text" name="edv" class="inputs" id="input4" placeholder="EDV">
        <input type="password" name="senha" class="inputs" id="input5" placeholder="Senha">
        <button>Enviar</button>
      </div>
    </div>
    <footers/>
  </div>
</template>

<script>

export default {
  name: 'home',
}

</script>

<style lang="scss" scoped>
  @import '@/pages/cadastro_usuario/cadastro_usuario.scss'
</style>