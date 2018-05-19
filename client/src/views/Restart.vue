<template>
   <div class="animated fadeIn">
    <div id="overall_info">
      <b-row>
        <b-col sm="6" md="4">
          <b-card class="card-accent-success" header="Card with accent">
            <div slot="header">
              活跃爬虫
              <b-badge variant="success" class="float-right">Ongoing</b-badge>
            </div>
            <h2>{{active_spider}}</h2>
            <p>个最近活跃爬虫</p>
          </b-card>
        </b-col>
        <b-col sm="6" md="4">
          <b-card class="card-accent-primary" header="Card with accent">
            <div slot="header">
              总爬虫数
              <b-badge variant="primary" class="float-right">Overall</b-badge>
            </div>
            <h2>{{overall_spider}}</h2>
            <p>个爬虫在爬虫池中</p>
          </b-card>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <el-button type="danger" @click="restart">重启全部爬虫</el-button>
        </b-col>
      </b-row>
    </div>
   </div>
</template>

<script>
export default {
  data: function () {
    return {
      active_spider: 0,
      overall_spider: 0,
      job_num: 0,
      chat_date: Date(),
      ongoing_job: 5,
      ongoing_task: 23,
      job_progress: '85%',
      task_progress: '60%'
    }
  },
  methods: {
    restart () {
      this.$confirm('此操作将暂停所有任务并重启爬虫, 是否继续?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        this.$message({
          type: 'active',
          message: '成功重启!'
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消'
        })
      })
    }
  }
}
</script>
