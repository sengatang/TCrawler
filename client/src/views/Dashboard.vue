<template>
  <div class="animated fadeIn">
    <div id="overall_info">
      <b-row>
        <b-col sm="6" md="4">
          <b-card class="card-accent-primary" header="Card with accent">
            <div slot="header">
              主机连接
              <b-badge variant="success" class="float-right">Success</b-badge>
            </div>
            <h2>{{success_num}}</h2>
            <p>个主机成功连接</p>
          </b-card>
        </b-col>
        <b-col sm="6" md="4">
          <b-card class="card-accent-primary" header="Card with accent">
            <div slot="header">
              主机连接
              <b-badge variant="danger" class="float-right">Error</b-badge>
            </div>
            <h2>{{error_num}}</h2>
            <p>个主机连接错误</p>
          </b-card>
        </b-col>
        <b-col sm="6" md="4">
          <b-card class="card-accent-primary" header="Card with accent">
            <div slot="header">
              任务进行
              <b-badge variant="primary" class="float-right">Ongoing</b-badge>
            </div>
            <h2>{{job_num}}</h2>
            <p>个任务正在进行中</p>
          </b-card>
        </b-col>
      </b-row>
    </div>
    <b-card>
      <b-row>
        <b-col sm="5">
          <h4 id="traffic" class="card-title mb-0">月爬虫执行情况</h4>
          <div class="small text-muted">{{chat_date}}</div>
        </b-col>
      </b-row>
      <main-chart-example class="chart-wrapper" style="height:300px;margin-top:40px;" height="300"></main-chart-example>
      <div slot="footer">
        <ul>
          <li>
            <div class="text-muted">Job Num</div>
            <strong>{{ongoing_job}} Jobs {{job_progress}} </strong>
            <b-progress height={} class="progress-xs mt-2" :precision="1" variant="success" :value="85"></b-progress>
          </li>
          <li class="d-none d-md-table-cell">
            <div class="text-muted">Task Num</div>
            <strong>{{ongoing_task}} Tasks {{task_progress}}</strong>
            <b-progress height={} class="progress-xs mt-2" :precision="1" variant="info" :value="60"></b-progress>
          </li>
        </ul>
      </div>
    </b-card>
  </div>
</template>

<script>

import MainChartExample from './dashboard/MainChartExample'

export default {
  name: 'dashboard',
  components: {
    MainChartExample
  },
  data: function () {
    return {
      success_num: 0,
      error_num: 0,
      job_num: 0,
      chat_date: Date(),
      ongoing_job: 5,
      ongoing_task: 23,
      job_progress: '85%',
      task_progress: '60%'
    }
  },
  methods: {
    variant (value) {
      let $variant
      if (value <= 25) {
        $variant = 'info'
      } else if (value > 25 && value <= 50) {
        $variant = 'success'
      } else if (value > 50 && value <= 75) {
        $variant = 'warning'
      } else if (value > 75 && value <= 100) {
        $variant = 'danger'
      }
      return $variant
    },
    flag (value) {
      return 'flag-icon flag-icon-' + value
    }
  }
}
</script>
