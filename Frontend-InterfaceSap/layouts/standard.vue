<template>
  <div class="layout_default">
    <headers/>
    <Nuxt/>
    <footers/>
  </div>
</template>

<script>
export default {
  name: 'standard',
}
</script>

<style lang="scss">
@import '@/layouts/variaveis.scss';

.layout_default {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  // width: 100vw;
  // max-width: 100vw;
  // min-width: 100vw;
  height: auto;
  min-height: 100vh;
  box-sizing: border-box;
  margin: 0;
}
</style>