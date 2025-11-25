## Obtaining figures

Using scipy's linear regression model, I got a line of best fit for the data of my videos in terms of average percentage viewed, impression click through rate, and likes. In simple terms, I got an equation that will give you the metric estimate based upon the views of a video. 

Here is the equation written in plain english that was obtained:
$$ metric=slope\cdot\ln\left(views\right)+intercept $$

Using this equation, we can solve for the metric, and thus we can predict how a change in a metric would, in theory, correlate with a change in views.

Here is that equation solved for views:
$$ views=e^{\left(\frac{metric-intercept}{slope}\right)} $$

## Figures themselves
Here are the values for $R^2$, $Slope$, $p$, $\sigma$, and $intercept$ for each metric.

| $Metric$ | $R^2$ | $Slope$ | $p$ | $\sigma$ | $Intercept$ |
| ---  | ---  | ---  | ----- | ----- | --- |
| Average Percentage Viewed | 0.10036064 | 3.77452481 | 0.00000003 | 0.66020830 | 14.67161831 |
| Impressions Click-through Rate (%) (whole) | 0.10159317 | 0.64519863 | 0.00000004 | 0.11385144 | -0.08569814 |
| Likes | 0.35550122 | 59.24532584 | 0.00000000 | 4.73353318 | -279.79888998 |

## Implications
For better understanding, I think the best way to convey these figures is in terms of what would result in a 10x increase in views. That is, to say, if a video had 1000 views, and it increased one metric by a certain value, it would be expected that the video would reach 10,000 views. There are many inherent flaws with this thinking, but it conveys the overall implication of these figures very well. I will follow these figures up with my personal thoughts about them.

## Percentage Viewed
#### Increasing a video's views by 10x would require increase your Average Percentage Viewed by 8.69117%

Increasing the average percentage viewed of a video is not easy, and it gets exponentially harder the higher the percentage actually is. I would say getting people to watch a quarter of a video or 25% on average requires a good idea that hooks viewers in. To get from that closer to half the video or 50% requires a quantum leap in editing skills, editing time, and really honing in on every single element of the video itself. I believe working on something like this is a good idea initially but as people get better and better at making videos this figure becomes more and more of a stick in the mud.

## Click-through Rate
#### Increasing a video's views by 10x would require increase your Impression Click-through Rate by 1.48562%

This is a much simpler figure to increase, but there is still so much underneith the surface of this statement. Click-through rate is how often your video is shown compared to how often your video is clicked on. Thus this figure comes from when your videos are trying to get the attention of a YouTube user who is at the same time able to see many other videos, which are also trying to get the user's attention. The main way to increase this is to have a good idea first and then convey it in an interesting and attention grabbing manner second, primarily though the video thumbnail and title.

## Likes
#### Increasing a video's views by 10x would require increase the likes on a video by 136.41741 or ~136 likes

This figure can be increased in a very passive and a very active way, but being too active about it can lead to adverse consequences. From what I've noticed, if people really enjoy how a video is edited, they feel most inclined to both comment and like the video. So just as before with percentage viewed, this really comes down to experience and effort. The other way to do this is to ask people to like the video or promise something on the conditions of reaching a certain amount of likes. It is almost impossible to see just how effective requesting likes can be, but as long as it is done in good taste it would not hurt to try.