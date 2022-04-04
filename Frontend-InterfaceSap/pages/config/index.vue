<template>
  <div class="cont">
        <div class="page">
          <div class="content-block">
            <div class="titulo">
              <h1>Configurações</h1>
              <hr>
            </div>
            <div class="cards">
              <div class="card-one c">
                <h1>Cadastrar Usuario</h1>
                <img src="/sucata.png">
                <NuxtLink class="btn-ir" to="/cadastro_usuario">Selecionar</NuxtLink>                
              </div>

              <div class="card-two c">
                <h1>Consultar Usuario</h1>
                <img src="/produto.png">
                <NuxtLink class="btn-ir" to="/consulta_usuario">Selecionar</NuxtLink>                
              </div>

              <div class="card-three c">
                <h1>Historico Usuario</h1>
                <img src="/sucata.png">
                <NuxtLink class="btn-ir" to="#">Selecionar</NuxtLink>                
              </div>
            </div>
          </div>
        </div>
  </div>
</template>

<script>
export default {
  name: "trancoes",
  layout: 'standard',
  // middleware: 'auth',
}
</script>

<style lang="scss" scoped>
  @import '@/pages/transacoes/transacoes.scss'
</style>