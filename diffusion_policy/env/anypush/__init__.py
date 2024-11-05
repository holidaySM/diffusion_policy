from gym.envs.registration import register
import diffusion_policy.env.anypush

register(
    id='anypush-keypoints-v0',
    entry_point='envs.anypush.anypush_keypoints_env:AnyPushKeypointsEnv',
    max_episode_steps=200,
    reward_threshold=1.0
)