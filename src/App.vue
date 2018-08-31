<template>
  <div>
    <el-steps :active="currentStep" simple>
      <el-step title="选择素材"></el-step>
      <el-step title="调整位置"></el-step>
      <el-step title="打印结果"></el-step>
    </el-steps>
    <div v-if="currentStep==0">
      <div class="guide"> 输入淘宝id获得个性化的推荐和搭配 </div>
      <div>
        <el-input width="250" v-model="taobaoId" placeholder="输入淘宝id"></el-input>
        <el-button type="primary"> 获取搭配 </el-button>
      </div>
      <div class="guide"> 或者，从下列商品中选择一个进行搭配</div>
      <item-selector style="margin: 0 50px 0 50px;"></item-selector>
    </div>
    <div v-else-if="currentStep==1">
      <div class="guide"> 为搭配好的内容选择合适的位置 </div>
      <el-card style="width: fit-content; margin: auto;">
        <item-placer style="width: 512px; height: 512px; position: relative;" ></item-placer>
      </el-card>
    </div>
    <div v-else>
      打印
    </div>
  </div>
</template>

<script>
import ItemSelector from './components/ItemSelector'
import ItemPlacer from './components/ItemPlacer'

export default {
  name: 'app',
  components: {
    ItemSelector,
    ItemPlacer
  },
  data() {
    return {
      currentStep: 1,
      taobaoId: ''
    }
  }
}
</script>

<style>
.guide {
  font-size: 18px;
  text-align: center;
  margin: 50px 0 50px 0;
}
</style>
