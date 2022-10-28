# simple_falldetection
<h2>あらまし</h2>
骨格検知後に得られる座標から通常状態(Normal)、転落状態(Fall)、回復・立ち上がり状態(Recovering)を判定するプログラムです。<br>
Openpose等適当なソフトを試したい方で、(x,y)座標を利用してとりあえず転倒判定を行なってみたいなと思っている方向けのものです。<br>
(x,y)座標を取得し前後の差分から状態を判定していますが、詳細なアルゴリズムについての説明は省きます。<br>
<br>
<h2>おおまかな仕組み:</h2>
1. 骨格検知ソフトから(x,y)座標を受け取る<br>
2. openCVでとりあえず座標を描画する。<br>
3. 座標の前後差分から状態を判定する。<br>
  <strong>このとき、以下のような制約をつけている。</strong>
  <ul>
  <li>転倒イベントの一連の動作は、<br>
    必ず Normal --> Fall --> Recovering --> Normal の順で発生しなければならず、<br>
    例えばNormal-->Recovering,Fall-->Normalといった状態遷移は行わない。</li>
  <li>a. 前後が　Fall --> Normal であった場合には、状態を Fall に書き換える。</li>
  <li>b.　　前後が Normal --> Recovering であった場合には、状態を Normal に書き換える。</li>
  <li>c. 前後が Recovering --> Fall であった場合には、状態をRecovering に書き換える。</li>
  </ul>
4. 取得した状態に応じて、各フレームごとにopenCVで画面左上に状態の描画を行う。<br>
5. 出力される骨格検知の動画に転倒判定が反映される。<br>
<br>
<h2>動かしてみたらこんな感じ</h2>
<br>
画像をクリックしたらyoutubeの動画に飛ぶよ。<br>
[![test_video](http://img.youtube.com/vi/9F2J1XaK-Iw/0.jpg)](http://www.youtube.com/watch?v=9F2J1XaK-Iw)





