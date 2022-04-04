// Consulta Usuario 

<template>
  <div class="cont">
    <headers/>
    <div class="principal">
      <div class="base">
        <h1>Consulta de Usuario</h1>
        <div class="centro">
          <input type="text" name="search" class="inputs" id="input1" placeholder="Pesquisar">        
          <button> Buscar </button>
        </div>
        <input type="text" name="searchs" value="" class="inputs" id="input2">
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
  @import '@/pages/consulta_usuario/consulta_usuario.scss'
</style>