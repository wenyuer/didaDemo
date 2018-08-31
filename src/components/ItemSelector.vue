<template>
  <div>
    <el-row id="item-row">
      <el-col class="item-col" :span="4" v-for="item in items">
        <el-card>
          <img src="../assets/dida_fish.png"></img>
          <el-button type="text"> 继续搭配 </el-button>
        </el-card>
      </el-col>
    </el-row>
    <div>
      <el-select v-model="type">
        <el-option value="0" label="上衣"></el-option>
        <el-option value="1" label="裤子"></el-option>
        <el-option value="2" label="鞋"></el-option>
        <el-option value="3" label="裙子"></el-option>
        <el-option value="4" label="帽子"></el-option>
        <el-option value="5" label="包"></el-option>
      </el-select>
      <el-button id="refresh" type="primary" icon="el-icon-refresh"> 换一批 </el-button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      items: [],
      type: "0"
    }
  },
  methods: {
    reload: function() {
      this.items = [1, 2, 3, 4, 5, 6]
    }
  },
  mounted: function() {
    this.reload()
  }
}
</script>

<style>
#item-row {
  margin-bottom: 10px;
}
.el-col:nth-child(n+2) .el-card {
  margin-left: 10px;
}
.el-card img {
  width: 100%;
  min-height: 150px;
}
#refresh {
  margin-left: 10px;
}
</style>
