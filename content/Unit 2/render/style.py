css = """<style>
.parent {
    position: relative;
    width: 100%;
    height: 100%;
    max-width: 800px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
    margin-left: auto;
    margin-right: auto;
    overflow: hidden;
}
.parent_bg {
    position: absolute;
    width: 100%;
    height: 100%;
}
.view_box {    
    box-sizing: content-box;
    border: 2px solid black;
    background-color: black;
    display: grid;
    grid-template-columns: auto;
    grid-template-rows: auto;
    width: fit-content;
    min-width: 480px;
    min-height: 270px;
    max-width: 480px;
    max-height: 270px;
    overflow: hidden;
}
.bg_stack{
    grid-column: 1;
	grid-row: 1;
}
.bg {    
    width: 100%;
    height: 100%;
    max-width: 475px;
    max-height: 265px;
}
.sprite_box {
    grid-column: 1;
	grid-row: 1;
    display: flex;
    width:100%;
    height:100%;
    align-items: flex-end;
    justify-content: space-between;
    padding: 10px 40px 10px 40px;
}
.btn_box {
    display: flex;
    justify-content: center;
    gap: 10px;
    margin: 10px;
}
.header_box {
    display: flex;
    width: 100%;
    margin: 10px;
    justify-content: space-between;
    gap: 5px;    
    font-weight: bold;
}
.ui_health {
}
.ui_label {
    width: 2em;
}
.ui_enemy {
}
.ui_meter_stack{
    width: fit-content;
}
.ui_meter{
    align-items: center;
    overflow: hidden;
}
.stage {
    position: relative;
    width:24px;
    height:32px;
}
.stage::before {
    content: "";
    width: 8px;
    height: 8px;
    border-radius: 20px;
    background-color: black;
    position: absolute;
    bottom: 0;
    left: 50%;
    opacity: 0.25;
}
.stage_stack {    
    width: 150px;
    bottom: 15px;
    justify-content: center;
}
.debug {
    border: 1px dashed red;
}
.ani_container {    
    display: flex;
    justify-content: center;
    align-items: center;
    overflow: hidden;
    position: relative;
    left: 0;
    transition: left 0.2s;
}
.enemy_stack {
    overflow:visible;
}
@keyframes bounceRight {
    0% {transform: translateX(0);}
    50% {transform: translateX(+100px);}
    100% {transform: translateX(0);}
}
.bounce_right {    
    animation: bounceRight 1s ;
}
@keyframes bounceLeft {
    0% {transform: translateX(0);}
    50% {transform: translateX(-100px);}
    100% {transform: translateX(0);}
}
.bounce_left {    
    animation: bounceLeft 1s ;
}
.stage_label {
    font-size: 1.5em;
    font-weight: bold;
    color: black;
}
</style>""" 

def apply_style():
    from IPython.display import HTML, display
    display(HTML(css))