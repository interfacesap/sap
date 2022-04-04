// Solicitação de Produtos

<template>
  <div class="cont">
    <headers/>
    <div class="principal">
      <form class="base">
        <h1>Solicitação de Produtos</h1>
        <div class="centro">
        <section class="img">
            <img src="/fita.png">
        </section>
        <section class="campos">
            <input type="text" name="material" class="inputs" id="material" placeholder="Numero do Material" v-model="solicitacao.material" required>
            <input type="text" name="quantidade" class="inputs" id="quantidade" placeholder="Quantidade(UN)" v-model="solicitacao.quantidade" required>
            <input type="text" name="recebedor" class="inputs" id="recebedor" placeholder="Recebedor" v-model="solicitacao.recebedor" required>
        </section>
        </div>
        <button type="submit" @click="fetchSolicitacao">Enviar</button>
      </form>
    </div>
    <footers/>
  </div>
</template>

<script>

export default {
  name: 'home',
  data() {
    return {
      solicitacao: {
        material: '',
        quantidade: '',
        recebedor: '',
        umr: 7463,
        dep: 555,
        idProdutoFK: 1,
        idCentroCFK: 2,
        idTipoMovimentoFK: 1,
        idContaRazaoFK: 1
      },
    }
  },
  methods: {
    fetchSolicitacao: async function () {
    let send = true
    
    for (const [key, value] of Object.entries(this.solicitacao)){
      if (document.getElementById(key)) {
        if (value == '') { 
          send = false
          document.getElementById(key).style.borderColor = 'red'
        } else {
          document.getElementById(key).style.borderColor = '#E5E5E5'
        }
      }
    }

    if(send){
      await this.$axios
      .$post(
        'http://127.0.0.1:8000/TransacaoProduto/',
        JSON.stringify([this.solicitacao]),
        {
          headers: {
            'Content-type': 'application/json',
          },
        }
      )
      .then((response) => {
        console.log(response)
      })
      .catch((error) => {  
        console.log(error)
      })
    }

    },
  },
}


</script>

<style lang="scss" scoped>
@import '@/pages/solicitacao_produto/solicitacao_produto.scss'
</style>