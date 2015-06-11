#include <clutter/clutter.h>
#include <stdlib.h>

ClutterActor *stage;
ClutterActor *car1;
gdouble translateSpeed;

void on_timeline_new_frame(ClutterTimeline *timeline, gint frame_num, gpointer data){
	translateSpeed+=1.5;
	clutter_actor_set_translation(car1,translateSpeed,0,0);
}

ClutterActor *create_car(ClutterColor col, ClutterActor *road){

	gfloat roadHeight = clutter_actor_get_height(road);
	gfloat roadWidth = clutter_actor_get_width(road);
	ClutterActor *rect = clutter_rectangle_new_with_color(&col);
	clutter_actor_set_size(rect,10,10);
	if(roadWidth>roadHeight) clutter_actor_set_position(rect,0,134+clutter_actor_get_x(road));
	else clutter_actor_set_position(rect,clutter_actor_get_y(road),0);
	clutter_container_add_actor(CLUTTER_CONTAINER(stage),rect);
	clutter_actor_show(rect);
	clutter_actor_set_anchor_point(rect,5,5);

	return rect;

}

ClutterActor *create_road(ClutterColor col, int pos, gboolean horzOrVert){

	ClutterActor *rect = clutter_rectangle_new_with_color(&col);
	if(horzOrVert) clutter_actor_set_size(rect,20,512);
	else clutter_actor_set_size(rect,512,20);
	if(horzOrVert) clutter_actor_set_position(rect,pos,0);
	else clutter_actor_set_position(rect,0,pos);
	//if(horzOrVert) clutter_actor_set_anchor_point(rect,10,256);
	//else clutter_actor_set_anchor_point(rect,256,10);
	clutter_container_add_actor(CLUTTER_CONTAINER(stage),rect);
	clutter_actor_show(rect);

	return rect;

}

ClutterActor *create_stoplight_cluster(int posx, int posy){
	ClutterColor yellow = {204,204,0,255};
	ClutterColor green = {0,255,0,255};
	ClutterColor red = {255,0,0,255};
	ClutterActor *sl[4];
	for(int i=0; i<4; i++){
		sl[i] = clutter_rectangle_new_with_color(&yellow);
		clutter_actor_set_size(sl[i],10,20);
		clutter_container_add_actor(CLUTTER_CONTAINER(stage),sl[i]);
	}
	clutter_actor_set_position(sl[0],posx-10-5,posy-10-15);
	clutter_actor_set_position(sl[1],posx+10+15,posy-10-15);
	clutter_actor_set_position(sl[2],posx-10-5,posy+10+15);
	clutter_actor_set_position(sl[3],posx+10+15,posy+10+15);

}

int main(int argc, char *argv[]) {
	clutter_init(&argc, &argv);

	ClutterColor stage_color = { 0, 0, 0, 255 };

	stage = clutter_stage_get_default();
	clutter_actor_set_size(stage, 512, 512);
	clutter_stage_set_color(CLUTTER_STAGE(stage), &stage_color);

	ClutterActor* roads[4];

	ClutterColor road_color = {192,192,192,255};
	ClutterColor car_color = {0,0,255,255};
	for(int i=0; i<2; i++){
		roads[i] = create_road(road_color,128,i);
		roads[i+2] = create_road(road_color,384,i);
	}
	create_stoplight_cluster(128,128);
	create_stoplight_cluster(384,384);

	car1 = create_car(car_color,roads[0]);

	ClutterTimeline *timeline = clutter_timeline_new(60);
	g_signal_connect(timeline,"new-frame", G_CALLBACK(on_timeline_new_frame),NULL);
	clutter_timeline_set_loop(timeline,TRUE);
	clutter_timeline_start(timeline);

	clutter_actor_show(stage);

	clutter_main();
	//g_object_unref(timeline);

	return EXIT_SUCCESS;
}